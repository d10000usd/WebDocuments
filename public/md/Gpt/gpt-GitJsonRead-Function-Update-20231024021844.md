# **<span style="font-size: 35px; font-style: italic;">GitJsonRead Function Update</span>**


<div class="body-full">

위의 코드에서는 프로미스가 반환됩니다. 이 프로미스는 `GitJsonRead` 함수가 호출될 때 생성되며, 내부적으로 fetch 작업을 수행합니다. fetch 작업이 성공하면 해당 파일의 텍스트 내용이 resolve로 반환됩니다. 그러나 fetch 작업이 실패하면 catch 블록이 실행되어 error가 reject로 반환됩니다.

따라서 `GitJsonRead` 함수는 프로미스를 반환하며, 이 프로미스는 fetch 작업이 성공 또는 실패할 때 적절한 값 또는 오류를 전달합니다.


</div>