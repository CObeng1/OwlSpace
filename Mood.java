public class Mood {
    private String moodName;
    private String playlist;
    private String image;
    private String description;

    public Mood(String moodName, String playlist, String image, String description) {
        this.moodName = moodName;
        this.playlist = playlist;
        this.image = image;
        this.description = description;
    }
    public String getMoodName() {
        return moodName;
    }
    public void setMoodName(String moodName) {
        this.moodName = moodName;
    }
    public String getPlaylist() {
        return playlist;
    }
    public void setPlaylist(String playlist) {
        this.playlist = playlist;
    }
    public String getImage() {
        return image;
    }
    public void setImage(String image) {
        this.image = image;
    }
    public String getDescription() {
        return description;
    }
    public void setDescription(String description) {
        this.description = description;
    }

}
