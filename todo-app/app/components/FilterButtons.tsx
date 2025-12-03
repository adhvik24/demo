'use client';

import { FilterType } from '../types';

interface FilterButtonsProps {
  filter: FilterType;
  setFilter: (filter: FilterType) => void;
  activeCount: number;
  completedCount: number;
}

export default function FilterButtons({
  filter,
  setFilter,
  activeCount,
  completedCount,
}: FilterButtonsProps) {
  const buttons: { label: string; value: FilterType; count?: number }[] = [
    { label: 'All', value: 'all' },
    { label: 'Active', value: 'active', count: activeCount },
    { label: 'Completed', value: 'completed', count: completedCount },
  ];

  return (
    <div className="flex gap-2 flex-wrap">
      {buttons.map(({ label, value, count }) => (
        <button
          key={value}
          onClick={() => setFilter(value)}
          className={`px-4 py-2 rounded-lg font-medium transition-all ${
            filter === value
              ? 'bg-blue-600 text-white dark:bg-blue-500'
              : 'bg-gray-200 text-gray-700 hover:bg-gray-300 dark:bg-gray-700 dark:text-gray-300 dark:hover:bg-gray-600'
          }`}
        >
          {label}
          {count !== undefined && (
            <span className="ml-1.5 text-sm opacity-75">({count})</span>
          )}
        </button>
      ))}
    </div>
  );
}
