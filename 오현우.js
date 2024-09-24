//오버레이
function toggleOverlay(overlayId) {
    var overlay = document.getElementById(overlayId);
    if (overlay.style.display === 'none' || overlay.style.display === '') {
        overlay.style.display = 'flex';
    } else {
        overlay.style.display = 'none';
    }
}

//가사검색 삭제
//입력값 0으로 바꾸기
function 삭제() {
    document.getElementById("인풋값").value=""
}

//배경색 
//0신호 받으면 파랑, 1신호 받으면 검정
var 색 = 0
function 색변화(색) {
    if (색 === 0) {
        document.body.style.backgroundColor = '#0063DC';
    } else if (색 === 1) {
        document.body.style.backgroundColor = 'black';
    }
}