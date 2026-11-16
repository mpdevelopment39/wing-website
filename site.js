// Progressive enhancement: screenshot links work directly without JavaScript.
const viewer = document.querySelector('.screenshot-dialog');
if (viewer && typeof viewer.showModal === 'function') {
  const image = viewer.querySelector('.dialog-image img');
  const caption = viewer.querySelector('#screenshot-caption');
  let previousOverflow = '';
  document.querySelectorAll('[data-screen]').forEach(link => {
    link.addEventListener('click', event => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      const source = link.querySelector('img');
      image.src = link.href;
      image.alt = source.alt;
      caption.textContent = source.alt;
      previousOverflow = document.body.style.overflow;
      document.body.style.overflow = 'hidden';
      viewer.showModal();
    });
  });
  viewer.querySelector('[data-close]').addEventListener('click', () => viewer.close());
  viewer.addEventListener('click', event => {
    if (event.target !== viewer) return;
    const bounds = viewer.getBoundingClientRect();
    if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) viewer.close();
  });
  viewer.addEventListener('close', () => {
    document.body.style.overflow = previousOverflow;
    image.removeAttribute('src');
  });
}
