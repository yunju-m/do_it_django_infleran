// 키보드의 입력이 넣고 빠질 때(onkeyup) 즉시 입력된 내용으로 바꾸고 계산하는 함수
function doSomething(){
    let a = document.getElementById("inputA").value;
    let b = document.getElementById("inputB").value; 
    document.getElementById("valueA").innerHTML = a;
    document.getElementById("valueB").innerHTML = b;
    document.getElementById("valueC").innerHTML = Number(a)+Number(b);  // Number는 str -> int 형변환
}