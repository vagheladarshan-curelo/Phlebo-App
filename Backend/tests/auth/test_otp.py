# tests/auth/test_otp.py
import pytest
from unittest.mock import patch, MagicMock
from app.auth.otp import send_otp, verify_otp


# ─── Fixtures ────────────────────────────────────────────────────────────────

@pytest.fixture
def valid_phone():
    return "9876543210"

@pytest.fixture
def invalid_phone():
    return "12345"  # too short

@pytest.fixture
def mock_send_success():
    """Times Messaging returns this on successful OTP send."""
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "status": "success",
        "message": "OTP sent successfully"
    }
    mock_response.status_code = 200
    return mock_response

@pytest.fixture
def mock_send_failure():
    """Times Messaging returns this when API key is wrong or limit hit."""
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "status": "error",
        "message": "Invalid API key"
    }
    mock_response.status_code = 401
    return mock_response

@pytest.fixture
def mock_verify_success():
    mock_response = MagicMock()
    mock_response.json.return_value = {"status": "success"}
    mock_response.status_code = 200
    return mock_response

@pytest.fixture
def mock_verify_failure():
    mock_response = MagicMock()
    mock_response.json.return_value = {"status": "error", "message": "Invalid OTP"}
    mock_response.status_code = 200
    return mock_response

@pytest.fixture
def mock_verify_expired():
    mock_response = MagicMock()
    mock_response.json.return_value = {"status": "error", "message": "OTP expired"}
    mock_response.status_code = 200
    return mock_response


# ─── Send OTP Tests ───────────────────────────────────────────────────────────

class TestSendOTP:

    def test_send_otp_success(self, valid_phone, mock_send_success):
        with patch("app.auth.otp.requests.post", return_value=mock_send_success):
            result = send_otp(phone=valid_phone)
            assert result["status"] == "success"

    def test_send_otp_calls_times_messaging_api(self, valid_phone, mock_send_success):
        """Verify the third-party API is actually being called."""
        with patch("app.auth.otp.requests.post", return_value=mock_send_success) as mock_post:
            send_otp(phone=valid_phone)
            mock_post.assert_called_once()

    def test_send_otp_passes_correct_phone(self, valid_phone, mock_send_success):
        """Phone number must be in the payload sent to Times Messaging."""
        with patch("app.auth.otp.requests.post", return_value=mock_send_success) as mock_post:
            send_otp(phone=valid_phone)
            call_kwargs = mock_post.call_args
            assert valid_phone in str(call_kwargs)

    def test_send_otp_invalid_api_key(self, valid_phone, mock_send_failure):
        with patch("app.auth.otp.requests.post", return_value=mock_send_failure):
            result = send_otp(phone=valid_phone)
            assert result["status"] == "error"

    def test_send_otp_raises_on_network_error(self, valid_phone):
        """If Times Messaging is unreachable, a connection error should propagate."""
        with patch("app.auth.otp.requests.post", side_effect=Exception("Network error")):
            with pytest.raises(Exception, match="Network error"):
                send_otp(phone=valid_phone)

    def test_send_otp_invalid_phone_format(self, invalid_phone):
        """Should raise ValueError before even calling the API."""
        with pytest.raises(ValueError):
            send_otp(phone=invalid_phone)


# ─── Verify OTP Tests ─────────────────────────────────────────────────────────

class TestVerifyOTP:

    def test_verify_otp_success(self, valid_phone, mock_verify_success):
        with patch("app.auth.otp.requests.post", return_value=mock_verify_success):
            result = verify_otp(phone=valid_phone, otp="123456")
            assert result is True

    def test_verify_otp_wrong_otp(self, valid_phone, mock_verify_failure):
        with patch("app.auth.otp.requests.post", return_value=mock_verify_failure):
            result = verify_otp(phone=valid_phone, otp="000000")
            assert result is False

    def test_verify_otp_expired(self, valid_phone, mock_verify_expired):
        with patch("app.auth.otp.requests.post", return_value=mock_verify_expired):
            result = verify_otp(phone=valid_phone, otp="123456")
            assert result is False

    def test_verify_otp_calls_times_messaging_api(self, valid_phone, mock_verify_success):
        with patch("app.auth.otp.requests.post", return_value=mock_verify_success) as mock_post:
            verify_otp(phone=valid_phone, otp="123456")
            mock_post.assert_called_once()

    def test_verify_otp_raises_on_network_error(self, valid_phone):
        with patch("app.auth.otp.requests.post", side_effect=Exception("Timeout")):
            with pytest.raises(Exception, match="Timeout"):
                verify_otp(phone=valid_phone, otp="123456")