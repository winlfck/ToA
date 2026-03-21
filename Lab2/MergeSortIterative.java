import java.util.Arrays;

public class MergeSortIterative {

    static int comparisonsCount = 0;
    static int writeCount = 0;

    public static void sort(int[] array) {
        int length = array.length;
        int iterationNumber = 1;

        for (int blockSize = 1; blockSize < length; blockSize *= 2) {
            System.out.println("\nОбробка підмасивів розміру " + blockSize + ":");

            for (int start = 0; start < length - 1; start += 2 * blockSize) {
                int middle = Math.min(start + blockSize - 1, length - 1);
                int end = Math.min(start + 2 * blockSize - 1, length - 1);

                if (middle < end) {
                    mergeParts(array, start, middle, end);
                    System.out.println("Крок " + iterationNumber + " [" + start + ", " + end + "]: "
                            + Arrays.toString(array));
                    iterationNumber++;
                }
            }
        }
    }

    public static void mergeParts(int[] array, int left, int middle, int right) {
        int leftSize = middle - left + 1;
        int rightSize = right - middle;

        int[] leftArray = new int[leftSize];
        int[] rightArray = new int[rightSize];

        for (int i = 0; i < leftSize; i++) {
            leftArray[i] = array[left + i];
        }

        for (int j = 0; j < rightSize; j++) {
            rightArray[j] = array[middle + 1 + j];
        }

        int i = 0;
        int j = 0;
        int index = left;

        while (i < leftSize && j < rightSize) {
            comparisonsCount++;

            if (leftArray[i] <= rightArray[j]) {
                array[index] = leftArray[i];
                i++;
            } else {
                array[index] = rightArray[j];
                j++;
            }

            index++;
            writeCount++;
        }

        while (i < leftSize) {
            array[index] = leftArray[i];
            i++;
            index++;
            writeCount++;
        }

        while (j < rightSize) {
            array[index] = rightArray[j];
            j++;
            index++;
            writeCount++;
        }
    }

    public static void main(String[] args) {
        int[] numbers = {69, 52, 97, 27, 10, 88, 29, 1, 24};

        System.out.println("Початковий масив: " + Arrays.toString(numbers));

        sort(numbers);

        System.out.println("\nВідсортований масив: " + Arrays.toString(numbers));
        System.out.println("\nКількість порівнянь: " + comparisonsCount);
        System.out.println("Кількість записів: " + writeCount);
    }
}
