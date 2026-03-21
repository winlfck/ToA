import java.util.Arrays;

public class QuickSort {

    static int comparisonsCount = 0;
    static int swapCount = 0;

    public static void sort(int[] array, int left, int right, int level) {
        printOffset(level);
        System.out.println("Виклик sort [" + left + "," + right + "]");

        if (left >= right) {
            printOffset(level);
            System.out.println("Підмасив має довжину 1 або менше, повернення");
            return;
        }

        int pivotIndex = partition(array, left, right, level);

        printOffset(level);
        System.out.println("Після partition опорний елемент на позиції " + pivotIndex
                + ", масив = " + Arrays.toString(array));

        sort(array, left, pivotIndex - 1, level + 1);
        sort(array, pivotIndex + 1, right, level + 1);
    }

    public static int partition(int[] array, int left, int right, int level) {
        int pivotValue = array[right];
        int smallerIndex = left - 1;

        printOffset(level);
        System.out.println("partition [" + left + "," + right + "], pivot = "
                + pivotValue + " (array[" + right + "])");

        for (int current = left; current < right; current++) {
            comparisonsCount++;

            printOffset(level + 1);
            System.out.print("Порівняння array[" + current + "]=" + array[current]
                    + " < " + pivotValue + " ? ");

            if (array[current] < pivotValue) {
                smallerIndex++;
                System.out.println("так, міняємо місцями " + smallerIndex + " і " + current);
                swapValues(array, smallerIndex, current, level + 1);
            } else {
                System.out.println("ні");
            }
        }

        printOffset(level);
        System.out.println("Переміщуємо опорний елемент: swap(" + (smallerIndex + 1) + "," + right + ")");
        swapValues(array, smallerIndex + 1, right, level + 1);

        return smallerIndex + 1;
    }

    public static void swapValues(int[] array, int first, int second, int level) {
        if (first == second) {
            printOffset(level);
            System.out.println("Обмін не потрібен, індекси однакові: " + Arrays.toString(array));
            return;
        }

        int temp = array[first];
        array[first] = array[second];
        array[second] = temp;
        swapCount++;

        printOffset(level);
        System.out.println("Після обміну: " + Arrays.toString(array));
    }

    public static void printOffset(int level) {
        for (int i = 0; i < level; i++) {
            System.out.print("    ");
        }
    }

    public static void main(String[] args) {
        int[] numbers = {69, 52, 97, 27, 10, 88, 29, 1, 24};

        System.out.println("Початковий масив: " + Arrays.toString(numbers));

        sort(numbers, 0, numbers.length - 1, 0);

        System.out.println("Відсортований масив: " + Arrays.toString(numbers));
        System.out.println("Кількість порівнянь: " + comparisonsCount);
        System.out.println("Кількість обмінів: " + swapCount);
    }
}
