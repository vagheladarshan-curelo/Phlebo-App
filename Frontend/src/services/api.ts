import { QueryClient } from '@tanstack/react-query';

export const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: 2,
      staleTime: 1000 * 60 * 5, // 5 minutes
    },
  },
});

// Example of a reusable API fetch function if needed
export const fetchApi = async (endpoint: string) => {
  const response = await fetch(`https://api.example.com/${endpoint}`);
  if (!response.ok) throw new Error('API request failed');
  return response.json();
};
