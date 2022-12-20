var todo = {
    init: function () {
        var _this = this;

        $("#frm_todo").on("submit", _this.create);
        $(".todo-toglle-status").on("change", _this.toggle);
        $(".btn-todo-remove").on("click", _this.remove);
    },
    create: function (e) {
        e.preventDefault();

        var $form = $(this);
        var content = $("[name=content]", $form).val();

        if (content.length === 0) {
            alert("내용을 입력해주세요!!");
            return false;
        }

        $.post("/api/v1/todo/", { content: content }, function (res) {
            if (res?.success) {
                location.href = "/";
            } else {
                alert("오류가 발생했습니다!!");
            }
        });

        return false;
    },
    toggle: function (e) {
        var $this = $(this);
        var todo_id = $this.data("id");

        $.ajax({
            url: `/api/v1/todo/${todo_id}`,
            method: "put",
            success: function (res) {
                if (!res?.success) {
                    alert("오류가 발생했습닏다!!");
                    location.reload();
                }
            },
            error: function (err) {
                alert("오류가 발생했습니다");
                location.reload();
            },
        });
    },
    remove: function (e) {
        e.preventDefault();

        var $this = $(this);
        var todo_id = $this.data("id");

        $.ajax({
            url: `/api/v1/todo/${todo_id}`,
            method: "delete",
            success: function (res) {
                if (!res?.success) {
                    alert("오류가 발생했습닏다!!");
                    location.reload();
                } else {
                    location.reload();
                }
            },
            error: function (err) {
                alert("오류가 발생했습니다");
                location.reload();
            },
        });

        console.log("remove");

        return false;
    },
};
todo.init();
