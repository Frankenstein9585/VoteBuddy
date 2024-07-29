let canvas = document.getElementById('canvas');
let context = canvas.getContext('2d');
let video = document.getElementById('video');
let capturedImage= document.getElementById('capturedImage');
let capture = document.getElementById('snap');
let retake = document.getElementById('retake');
let image_byte_string = document.getElementById('image_byte_string')

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
    image_byte_string.value = capturedImage.src;
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


