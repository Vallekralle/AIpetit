const exampleModal = document.getElementById('exampleModal')
  if (exampleModal) {
    exampleModal.addEventListener('show.bs.modal', event => {
      // Give button the id as value
      const button = event.relatedTarget;
      const changeBtnEl = document.getElementById('changeBtn');
      const id = button.getAttribute('data-bs-id');
      changeBtn.value = id;

      const text = button.getAttribute('data-bs-text');

      const modalTitle = exampleModal.querySelector('.modal-title');
      const modalBodyInput = document.getElementById('id_text');

      modalTitle.textContent = `Stichpunkt bearbeiten`;
      modalBodyInput.value = text;
    })
}