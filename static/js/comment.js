$(document).ready(function(){
    $(".wi-comment-btn").click(function(){
        console.log('btn click');
        var btn = $(this);
        var parent = btn.parent();
        var blog_id = parent.find('.wi-comment-blog-id').val();
        var content = parent.find('.wi-comment-content').val();

        var comment = {
            'blog_id': blog_id,
            'content': content
        };

        var request = {
            url: '/api/comment/add',
            type: 'post',
            data: comment,
            success: function() {
                var response = arguments[0];
                var c = JSON.parse(response);
                var username = c.username;
                var content = c.content;
                var time = c.created_time
                if(content == '') {
                    content = '无内容'
                }
                var cell = `
                    <div class="wi-comment-cell">
                        <div class="wi-comment-cell-user">
                            <span>${username}</span>
                            &nbsp;|&nbsp;
                            <span>${time}</span>
                        </div>
                        <div class="wi-comment-cell-connent">
                            ${content}
                        </div>
                    </div>
                    `;
                parent.before(cell);

            },
            error: function() {
                console.log('错误', arguments)
            }
        };
        $.ajax(request);
    });
});
