const addForm = document.getElementById('add-form');
const homeContainer = document.getElementById('home');
const notesContainer = document.getElementById('notes');
const noteBox = document.getElementById('note-box');
const editForm = document.getElementById('edit-form');
const title = document.getElementById('new-title');
const description = document.getElementById('new-description');
const alert = document.getElementById('alert');
const editAlert = document.getElementById('edit-alert');
const searchForm = document.getElementById('search-form')
const input = document.getElementById('input')
const icon = document.getElementById('icon')
const notes = JSON.parse(localStorage.getItem('notes')) || []

let editIndex;

addForm.addEventListener('submit', (e) => {
    e.preventDefault();
    let note = {
        title: e.target.title.value,
        description: e.target.description.value
    }
    addNote(note);
    addForm.reset();
})

const showAlert = (msg) => {
    alert.innerHTML = msg;
    alert.style.display="block"
    setTimeout(()=>{

        alert.style.display="none"
    },2000)
}

const addNote = (note) => {
    notes.push(note);
    showAlert("Note Added 😊")
    updateLs()
}

const updateLs = () => {
    localStorage.setItem('notes', JSON.stringify(notes));
    fetchNotes();
}

const displayHome = () => {
    homeContainer.style.display = "block"
    notesContainer.style.display = "none"
}

const displayNotes = () => {
    homeContainer.style.display = "none"
    notesContainer.style.display = "block"
}

const fetchNotes = () => {
    if(notes.length===0){
        noteBox.innerHTML = "<p class='fs-5 text-center text-danger'>Nothing to display!!</p>";
        return
    }
    noteBox.innerHTML = "";

    notes.forEach((note, index) => {
        let card = document.createElement('div')
        card.classList.add('card', 'p-3', 'my-3');
        card.innerHTML = `
     <h5 class="card-title">${note.title}</h5>
                    <p class="card-text">${note.description}</p>
                    <div class="d-flex gap-2">
                        <button class="btn btn-danger"><i class="fa-solid fa-trash"></i></button>
                        <button class="btn btn-info" data-bs-toggle="modal" data-bs-target="#exampleModal"><i class="fa-solid fa-edit"></i></button>
                    </div>
     
     
     `
        noteBox.appendChild(card);
        card.querySelector('.btn-danger').addEventListener('click', () => {

            notes.splice(index, 1);
            showAlert("Note Removed😊")
            updateLs()
        })
        card.querySelector('.btn-info').addEventListener('click', () => {
            title.value = note.title
            description.value = note.description
            editIndex = index;

        })

    })
}

editForm.addEventListener('submit',(e)=>{
    e.preventDefault();
    notes[editIndex].title = title.value;
    notes[editIndex].description = description.value;
    editAlert.style.display="block"
    setTimeout(()=>{
    editAlert.style.display="none"
    },2000)
    editForm.reset();
    
    updateLs();
})

searchForm.addEventListener('submit',(e)=>{
    e.preventDefault();
    const searchTerm = input.value.toUpperCase();
    document.querySelectorAll('.card-title').forEach(title=>{
        if(title.textContent.toUpperCase().includes(searchTerm)){
            title.parentElement.style.display="block"
        }else{
            title.parentElement.style.display="none"
        }
    })
})

const toggleMenu = () =>{
    if(icon.classList.contains('fa-bars')){
        icon.classList.replace('fa-bars','fa-xmark')
       
    }else {
        icon.classList.replace('fa-xmark','fa-bars')
    }
   
}
fetchNotes()