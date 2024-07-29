const video = document.getElementById('camera-preview');
const toggleCameraButton = document.getElementById('toggle-camera-btn');
const captureButton = document.getElementById('capture-btn');
const capturedImageCanvas = document.getElementById('captured-image');
const submitButton = document.getElementById('submit-btn');
let isFrontCamera = false;

// switch between front and back cameras
async function toggleCamera() {
    const devices = await navigator.mediaDevices.enumerateDevices();
    const videoDevices = devices.filter(device => device.kind === 'videoinput');

    if (videoDevices.length >= 2) {
        isFrontCamera = !isFrontCamera;
       const selectedDevice = isFrontCamera ? videoDevices[1] : videoDevices[0];
        // const selectedDevice = isFrontCamera ? videoDevices.find(device => device.label.includes('front')) : videoDevices[0];

       const constraints = {
           video: {
               deviceId: {
                   exact: selectedDevice.deviceId
               },
               facingMode: 'environment',
           }
       };
        // const constraints = { video: { deviceId: selectedDevice.deviceId ? { exact: selectedDevice.deviceId } : undefined } };

        navigator.mediaDevices.getUserMedia(constraints)
            .then((stream) => {
                video.srcObject = stream;
            })
            .catch((error) => {
                console.error('Error accessing camera: ', error);
            });
    }
}

// Get camera feed
navigator.mediaDevices.getUserMedia({ video: true })
.then((stream) => {
    video.srcObject = stream;
})
.catch((error) => {
    console.error('Error accessing camera: ', error);
});

// Toggle Camera Button Event Listener
toggleCameraButton.addEventListener('click', toggleCamera);


// Capture image from camera
captureButton.addEventListener('click', () => {
    capturedImageCanvas.width = video.videoWidth;
    capturedImageCanvas.height = video.videoHeight;
    capturedImageCanvas.getContext('2d').drawImage(video, 0, 0, video.videoWidth, video.videoHeight);
    capturedImageCanvas.style.display = 'block';
    submitButton.style.display = 'block';
});

// Submit Image to Flask Application Server
submitButton.addEventListener('click', () => {
    const imageData = capturedImageCanvas.toDataURL('image.jpeg');

    const formData = new FormData();
    formData.append('image', imageData);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => console.log('Server Response: ', data))
        .catch(error => console.error('Error sending image data: ', error))
});