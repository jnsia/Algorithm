import java.util.*;

class Solution {
    class File {
        int index;
        String head;
        int number;
        
        File (int index, String head, int number) {
            this.index = index;
            this.head = head;
            this.number = number;
        }
    }
    
    public String[] solution(String[] files) {
        int index = 0;
        
        List<File> fileArray = new ArrayList<>();
        
        for (String fileName: files) {
            File file = splitFileName(index++, fileName);
            // System.out.println(file.head + " " + file.number);
            fileArray.add(file);
        }
        
        Collections.sort(fileArray, new FileComparator());
        
        String[] answer = new String[files.length];
        index = 0;
        
        for (File file: fileArray) {
            System.out.println(files[file.index]);
            answer[index++] = files[file.index];
        }
        
        return answer;
    }
    
    class FileComparator implements Comparator<File> {
        @Override
        public int compare(File o1, File o2) {
            if (o1.head.compareTo(o2.head) > 0) {
                return 1;
            } else if (o1.head.compareTo(o2.head) < 0) {
                return -1;
            } else {
                return o1.number - o2.number;
            }
        }
    }
    
    private File splitFileName(int index, String fileName) {
        int order = 0;
        int count = 0;
        
        String head = "";
        String number = "";
        
        for (int i = 0; i < fileName.length(); i++) {
            char word = fileName.charAt(i);
            
            if ((int) word >= 48 && (int) word < 58) {
                if (order == 0) {
                    order = 1;
                    number += word;
                } else {
                    number += word;
                    if (number.length() >= 5) break;
                }
            } else {
                if (order == 1) break;
                else {
                    head += word;
                }
            }
        }
        
        return new File(index, head.toUpperCase(), Integer.parseInt(number));
    }
}