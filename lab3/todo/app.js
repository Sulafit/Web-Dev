// Get the input and list elements from the HTML
const newItemInput = document.getElementById('new-item-input');
const todoList = document.getElementById('todo-list');

// Define an array to hold our to-do items
let items = [];

// Function to add a new item to the list
function addItem() {
  const newItem = newItemInput.value.trim();
  if (newItem !== '') {
    items.push(newItem);
    renderList();
    newItemInput.value = '';
  }
}

// Function to mark an item as done
function markAsDone(index) {
  items[index] = items[index] + ' (done)';
  renderList();
}

// Function to delete an item from the list
function deleteItem(index) {
  items.splice(index, 1);
  renderList();
}

// Function to render the list
function renderList() {
  todoList.innerHTML = '';
  for (let i = 0; i < items.length; i++) {
    const item = items[i];
    const li = document.createElement('li');
    li.innerText = item;
    if (item.endsWith('(done)')) {
      li.classList.add('done');
    } else {
      const doneBtn = document.createElement('button');
      doneBtn.innerText = 'Done';
      doneBtn.addEventListener('click', () => markAsDone(i));
      li.appendChild(doneBtn);

      const deleteBtn = document.createElement('button');
      deleteBtn.innerText = 'Delete';
      deleteBtn.addEventListener('click', () => deleteItem(i));
      li.appendChild(deleteBtn);
    }
    todoList.appendChild(li);
  }
}

// Render the initial list
renderList();
