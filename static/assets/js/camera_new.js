let canvas = document.getElementById('canvas');
let context = canvas.getContext('2d');
let video = document.getElementById('video');
let capturedImage= document.getElementById('capturedImage');
let capture = document.getElementById('snap');
let retake = document.getElementById('retake');
let registerForm = document.getElementById('registerForm')

if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia()) {
navigator.mediaDevices.getUserMedia({video: {facingMode: 'environment'}})
    .then(stream => {
        video.srcObject = stream;
        video.play();
    });

video.addEventListener('loadedmetadata', () => {
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
});
}

capture.addEventListener('click', () => {
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    canvas.style.display ='none'

    capturedImage.src = canvas.toDataURL('image/jpg');
    capturedImage.style.display = 'block';
    capturedImage.style.width = '100%';
    capturedImage.style.height = 'auto';


    video.style.display = 'none';

    capture.style.display = 'none';
    retake.style.display = 'block';
});

retake.addEventListener('click', () => {
    video.style.display = 'block';
    capturedImage.style.display = 'none';
    capture.style.display = 'block';
    retake.style.display = 'none';
});

registerForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(registerForm);
    formData.append('capturedImageData', canvas.toDataURL('image/jpg'));

    fetch('/submit', {
        method: 'POST',
        body: formData
    })
        .then(response => response.text())
        .then(data => console.log(data))
        .catch(error => console.error('Error: ', error));
})

