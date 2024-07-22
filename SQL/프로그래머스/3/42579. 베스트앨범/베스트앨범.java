import java.util.*;

class Solution {
    class Genre {
        String genre;
        int playedNumber;
        
        Genre(String genre, int playedNumber) {
            this.genre = genre;
            this.playedNumber = playedNumber;
        }
    }
    
    class Song {
        int uniqueNumber;
        int playedNumber;
        
        Song(int uniqueNumber, int playedNumber) {
            this.uniqueNumber = uniqueNumber;
            this.playedNumber = playedNumber;
        }
    }
    
    public int[] solution(String[] genres, int[] plays) {
        Map<String, Integer> genreMap = new HashMap<>();
        Map<String, ArrayList<Song>> songMap = new HashMap<>();
        
        for (String genre: genres) {
            genreMap.put(genre, 0);
            songMap.put(genre, new ArrayList<>());
        }
        
        for (int i = 0; i < genres.length; i++) {
            String genre = genres[i];
            int play = plays[i];
            
            Song newSong = new Song(i, play);
            
            int totalPlayedNumber = genreMap.get(genre);
            ArrayList<Song> songs = songMap.get(genre);
            
            genreMap.put(genre, totalPlayedNumber + play);
            songs.add(newSong);
        }
        
        List<Genre> genreArray = new ArrayList<>();
        
        for (String genre: genreMap.keySet()) {
            Genre newGenre = new Genre(genre, genreMap.get(genre));
            genreArray.add(newGenre);
        }
        
        Collections.sort(genreArray, new GenreComparator());

        List<Integer> result = new ArrayList<>();
        
        for (Genre genre: genreArray) {
            ArrayList<Song> playedSongs = songMap.get(genre.genre);
            
            Collections.sort(playedSongs, new SongComparator());
            
            if (playedSongs.size() >= 2) {
                result.add(playedSongs.get(0).uniqueNumber);
                result.add(playedSongs.get(1).uniqueNumber);
            } else if (playedSongs.size() == 1) {
                result.add(playedSongs.get(0).uniqueNumber);
            }
        }
        
        int[] answer = new int[result.size()];
        
        for (int i = 0; i < answer.length; i++) {
            answer[i] = result.get(i);
        } 
        
        return answer;
    }
    
    class GenreComparator implements Comparator<Genre> {
        @Override
        public int compare(Genre o1, Genre o2) {
            return o2.playedNumber - o1.playedNumber;
        }
    }
    
    class SongComparator implements Comparator<Song> {
        @Override
        public int compare(Song o1, Song o2) {
            
            if (o1.playedNumber == o2.playedNumber) {
                return o1.uniqueNumber - o2.uniqueNumber;
            }
            
            return o2.playedNumber - o1.playedNumber;
        }
    }
}