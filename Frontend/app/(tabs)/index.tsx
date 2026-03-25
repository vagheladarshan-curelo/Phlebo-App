import React from 'react';
import { View, Text, FlatList, ActivityIndicator, TouchableOpacity, ListRenderItem } from 'react-native';
import { useQuery } from '@tanstack/react-query';
import { useUserStore } from '../../src/store/useUserStore';

interface User {
  id: number;
  name: string;
  email: string;
}

const fetchUsers = async (): Promise<User[]> => {
  const response = await fetch('https://jsonplaceholder.typicode.com/users');
  if (!response.ok) throw new Error('Network response was not ok');
  return response.json();
};

export default function HomeScreen() {
  const { data, isLoading, error, refetch } = useQuery<User[], Error>({
    queryKey: ['users'],
    queryFn: fetchUsers,
  });

  const { name, setName } = useUserStore();

  const renderItem: ListRenderItem<User> = ({ item }) => (
    <View className="p-4 mb-2 bg-white rounded-lg border border-gray-100">
      <Text className="font-semibold text-gray-800">{item.name}</Text>
      <Text className="text-gray-500">{item.email}</Text>
    </View>
  );

  if (isLoading) return <ActivityIndicator className="mt-20" size="large" />;
  if (error) return <Text className="mt-20 text-center text-red-500">Error: {error.message}</Text>;

  return (
    <View className="flex-1 p-4 bg-gray-50">
      <View className="mb-6 p-4 bg-white rounded-lg shadow-sm border border-gray-100">
        <Text className="text-xl font-bold text-gray-800">Hello, {name}!</Text>
        <TouchableOpacity 
          className="mt-2 p-2 bg-blue-500 rounded"
          onPress={() => setName('Expert Dev')}
        >
          <Text className="text-white text-center">Change Name</Text>
        </TouchableOpacity>
      </View>

      <Text className="mb-2 text-lg font-semibold text-gray-700">Sample User List (TanStack Query):</Text>
      <FlatList
        data={data}
        keyExtractor={(item) => item.id.toString()}
        renderItem={renderItem}
        onRefresh={refetch}
        refreshing={isLoading}
      />
    </View>
  );
}
