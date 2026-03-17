/**
 * someCamelCaseLabel -> Some Camel Case Label
 * @param label The camelCase label to format
 * @returns The Formatted Label
 */
export const formatLabel = (label: string) => {
  return `${label.charAt(0).toUpperCase()}${label
    .slice(1)
    .split(/(?=[A-Z])/)
    .join(' ')}`;
};
