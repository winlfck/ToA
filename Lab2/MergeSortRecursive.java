import java.util.Arrays;

public class MergeSortRecursive {

    static int comparisonsCount = 0;
    static int writeCount = 0;
    static int actionNumber = 1;

    public static void sort(int[] array, int left, int right, int level) {
        printOffset(level);
        System.out.println("Крок " + actionNumber++ + " | межі [" + left + ", " + right + "] : "
                + Arrays.toString(Arrays.copyOfRange(array, left, right + 1)));

        if (left >= right) {
            printOffset(level);
            System.out.println("Підмасив має 1 елемент, повертаємось: "
                    + Arrays.toString(Arrays.copyOfRange(array, left, right + 1)));
            return;
        }

        int middle = (left + right) / 2;

        printOffset(level);
        System.out.println("Поділ на частини: ліва [" + left + ", " + middle + "] "
                + Arrays.toString(Arrays.copyOfRange(array, left, middle + 1))
                + " | права [" + (middle + 1) + ", " + right + "] "
                + Arrays.toString(Arrays.copyOfRange(array, middle + 1, right + 1)));

        sort(array, left, middle, level + 1);
        sort(array, middle + 1, right, level + 1);

        mergeSections(array, left, middle, right, level);
    }

    public static void mergeSections(int[] array, int left, int middle, int right, int level) {
        int leftLength = middle - left + 1;
        int rightLength = right - middle;

        int[] leftPart = new int[leftLength];
        int[] rightPart = new int[rightLength];

        for (int i = 0; i < leftLength; i++) {
            leftPart[i] = array[left + i];
        }

        for (int j = 0; j < rightLength; j++) {
            rightPart[j] = array[middle + 1 + j];
        }

        printOffset(level);
        System.out.println("Злиття частин: " + Arrays.toString(leftPart) + " + " + Arrays.toString(rightPart));

        int i = 0;
        int j = 0;
        int index = left;

        while (i < leftLength && j < rightLength) {
            comparisonsCount++;

            printOffset(level + 1);
            System.out.print("Порівняння " + leftPart[i] + " <= " + rightPart[j] + " -> ");

            if (leftPart[i] <= rightPart[j]) {
                array[index] = leftPart[i];
                System.out.println("беремо " + leftPart[i] + " з лівої частини");
                i++;
            } else {
                array[index] = rightPart[j];
                System.out.println("беремо " + rightPart[j] + " з правої частини");
                j++;
            }

            index++;
            writeCount++;
        }

        while (i < leftLength) {
            array[index] = leftPart[i];
            printOffset(level + 1);
            System.out.println("Додаємо залишок з лівої частини: " + leftPart[i]);
            i++;
            index++;
            writeCount++;
        }

        while (j < rightLength) {
            array[index] = rightPart[j];
            printOffset(level + 1);
            System.out.println("Додаємо залишок з правої частини: " + rightPart[j]);
            j++;
            index++;
            writeCount++;
        }

        printOffset(level);
        System.out.println("Після злиття [" + left + ", " + right + "]: "
                + Arrays.toString(Arrays.copyOfRange(array, left, right + 1))
                + " | порівнянь=" + comparisonsCount + " записів=" + writeCount);
    }

    private static void printOffset(int level) {
        for (int i = 0; i < level; i++) {
            System.out.print("    ");
        }
    }

    public static void main(String[] args) {
        int[] numbers = {69, 52, 97, 27, 10, 88, 29, 1, 24};

        System.out.println("Початковий масив: " + Arrays.toString(numbers));

        sort(numbers, 0, numbers.length - 1, 0);

        System.out.println("\nРезультат:");
        System.out.println("Відсортований масив: " + Arrays.toString(numbers));
        System.out.println("Загальна кількість порівнянь: " + comparisonsCount);
        System.out.println("Загальна кількість записів: " + writeCount);
    }
}
