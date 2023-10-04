let songs = [
  {
    name: "Rang Lageya",
    path: "mp3/Rang-Lageya.mp3",
    src: "images/rang-lageya.jpg",
    singerName:"Mohit Chauhan, Rochak Kohli"
  },
  {
    name: "Tujhko Main Rakh Loon Wahan",
    path: "mp3/Tujhko-Main-Rakh-Loon-Wahan(PagalWorldl).mp3",
    src: "images/hawaye.jpg",
    singerName:"Arijit Singh"
  },
  {
    name: "Tum Se Hi",
    path: "mp3/Tum Se Hi.mp3",
    src: "images/tumsehi.jpg",
    singerName:"Mohit Chauhan"
  },
  {
    name: "Pee Loon Hoto ki sargam",
    path: "mp3/Pee-Loon-Hoto-Ki-Sargam(PagalWorldl).mp3",
    src: "images/peeloon.jpg",
    singerName:"Mohit Chauhan"
  },
  {
    name: "Jiya Dhadak Dhadak Jaye",
    path: "mp3/Jiya-Dhadak-Dhadak-Jaye(PagalWorldl).mp3",
    src: "images/jiyadhadak.jpg",
    singerName:"Rahat Fateh Ali Khan"
  },
  {
    name: "Jud Gayi Jud Gayi",
    path: "mp3/Jud-Gayi-Jud-Gayi-Tujhse-Yeh-Meri-Zindagi(PagalWorldl).mp3",
    src: "images/judgayi.jpg",
    singerName:"Rahat Fateh Ali Khan"
  },
  {
    name: "Malang Sajna",
    path: "mp3/malang.mp3",
    src: "images/malang.jpg",
    singerName:"Sachet Tandon, Parampara Tandon"
  },
  {
    name: "Bairiya",
    path: "mp3/Bairiya(PagalWorld.com.se).mp3",
    src: "images/bairaiya.jpg",
    singerName:"Arijit Singh"
  },
  {
    name: "Raatan Lambiyan",
    path: "mp3/Raatan Lambiyan(PagalWorld.com.se).mp3",
    src: "images/raatanlambiyan.jpg",
    singerName:"Arijit Singh"
  },
  {
    name: "Mere Sapno Ki Galiyon Mein",
    path: "mp3/Mere Sapno Ki Galiyon Mein(PagalWorld.com.se).mp3",
    src: "images/ranjhanave.jpg",
    singerName:"Antara Mitra, Soham Naik"
  },
  {
    name: "Kahani Suno",
    path: "mp3/Kahani Suno(PagalWorld.com.se).mp3",
    src: "images/kahanisuno.jpg",
    singerName:"Kaifi Khalil"
  },
  {
    name: "Chand Teri",
    path: "mp3/Chand Teri Roshni Ka(PagalWorld.com.se).mp3",
    src: "images/chandteri.jpg",
    singerName:"K K"
  },
  

  {
    name: "Tere Hawaale",
    path: "mp3/Tere Hawaale(PagalWorld.com.se).mp3",
    src: "images/hawale.jpg",
    singerName:"Arijit Singh"
  },

    {
      name: "Wafa Ne Bewafai",
      path: "mp3/wafa.mp3",
      src: "images/wafa.jpg",
      singerName:"Arijit Singh"
    },
    {
      name: "Kesariya",
      path: "mp3/kesariya.mp3",
      src: "images/kesariya.jpg",
      singerName:"Arijit Singh"
    },
    {
      name: "Maan Meri Jaan",
      path: "mp3/maanmeri.mp3",
      src: "images/manmeri.jpg",
      singerName:"king"
    },
    {
      name: "Let Me Down Slowly",
      path: "mp3/letmedown.mp3",
      src: "images/letme.jpg",
      singerName:"Alec Benjamin, Arijit Singh"
    },
   
   
  ];
  
  const prevBtn = document.getElementById('prev-btn');
  const playPauseBtn = document.getElementById('play-pause-btn');
  const nextBtn = document.getElementById('next-btn');
  const myaudio = document.getElementById('audio');
  const poster = document.getElementById('poster');
  const songName = document.getElementById('song-name')
  const singerName = document.getElementById('singer-name')
  const currentTime = document.getElementById('current-time');

  let currentSongIndex = 0;
  let isPlaying = false;
  
  function loadSong(index) {
    const song = songs[index];
    myaudio.src = song.path;
    poster.src = song.src;
    songName.innerHTML = song.name;
    singerName.innerHTML = song.singerName;
  
    if (isPlaying) {
      myaudio.play();
    }
  }
  
  function playPauseSong() {
    if (myaudio.paused) {
      myaudio.play();
      playPauseBtn.classList.replace('fa-play', 'fa-pause');
      isPlaying = true;
    } else {
      myaudio.pause();
      playPauseBtn.classList.replace('fa-pause', 'fa-play');
      isPlaying = false;
    }
  }
  
  prevBtn.addEventListener('click', () => {
    currentSongIndex = (currentSongIndex - 1 + songs.length) % songs.length;
    loadSong(currentSongIndex);
  });
  
  playPauseBtn.addEventListener('click', () => {
    playPauseSong();
  });
  
  nextBtn.addEventListener('click', () => {
    currentSongIndex = (currentSongIndex + 1) % songs.length;
    loadSong(currentSongIndex);
  });
  
  myaudio.addEventListener('ended', () => {
    // Automatically play the next song
    currentSongIndex = (currentSongIndex + 1) % songs.length;
    loadSong(currentSongIndex);
  });
 
  
 
  
 
  
  // Load the initial song
  loadSong(currentSongIndex);
  