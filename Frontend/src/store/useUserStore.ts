import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';
import AsyncStorage from '@react-native-async-storage/async-storage';

interface UserState {
  name: string;
  setName: (name: string) => void;
}

export const useUserStore = create<UserState>()(
  persist(
    (set) => ({
      name: 'Phlebo User',
      setName: (name: string) => set({ name }),
    }),
    {
      name: 'user-storage',
      storage: createJSONStorage(() => AsyncStorage),
    }
  )
);
