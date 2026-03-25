# Phlebo-App Frontend

This frontend is built with a modern, high-performance expert stack:
- **Framework**: Expo SDK 55+
- **Navigation**: Expo Router (File-based, (tabs) layout)
- **Styling**: NativeWind v4 (Tailwind CSS)
- **State (Server)**: TanStack Query (v5)
- **State (Client)**: Zustand (with MMKV persistence)
- **Storage**: react-native-mmkv

## Features Implemented

1.  **File-based Routing**: Root layout at `app/_layout.tsx` and tabs layout at `app/(tabs)/_layout.tsx`.
2.  **NativeWind v4**: Configured with `tailwind.config.js`, `babel.config.js`, `metro.config.js`, and `global.css`.
3.  **TanStack Query**: Sample fetch implementation in `app/(tabs)/index.tsx`.
4.  **Zustand + MMKV**: Global state management with persistent storage in `src/store/useUserStore.ts`.

## Getting Started

1.  Navigate to the directory:
    ```bash
    cd Frontend
    ```

2.  Install dependencies:
    ```bash
    npm install
    ```

3.  Run the application in Expo Go:
    ```bash
    npx expo start -c
    ```

## Directory Structure

- `/app`: Expo Router files (navigation, screens, layouts).
- `/components`: Atomic UI components.
- `/hooks`: Custom hooks for reusable logic.
- `/src/store`: Zustand slices and persistent state configuration.
- `/src/services`: API configurations and TanStack Query setup.
- `/theme`: Global styling constants and theme configuration.
