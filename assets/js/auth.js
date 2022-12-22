var auth = {
    init: function () {
        var _this = this;

        $("#frm_signin").on("submit", _this.handleSubmit);
    },
    handleSubmit: function (e) {
        e.preventDefault();

        try {
            var $form = $(this);
            var email_regex = new RegExp("[a-z0-9]+@[a-z]+.[a-z]{2,3}");
            var data = {
                email: $('[name="email"]', $form).val().trim(),
                password: $('[name="password"]', $form).val().trim(),
            };

            if (data.email.length === 0) {
                throw new Error("이메일을 입력해주세요!!");
            }
            if (!email_regex.test(data.email)) {
                throw new Error("올바른 이메일을 입력해주세요!!");
            }
            if (data.password.length === 0) {
                throw new Error("비밀번호를 입력해주세요!!");
            }

            $.ajax({
                url: "/api/v1/auth/",
                type: "post",
                dataType: "json",
                contentType: "application/json",
                data: JSON.stringify(data),
                success: function (res) {
                    try {
                        if (res.success) {
                            alert("로그인되었습니다!!");
                            location.href = "/";
                        } else {
                            throw new Error(res.message);
                        }
                    } catch (e) {
                        alert(e?.message || "오류가 발생했습니다!!");
                    }
                },
                error: function (err) {
                    alert("오류가 발생했습니다!!");
                },
            });
        } catch (e) {
            alert(e?.message || "오류가 발생했습니다!!");
        }

        return false;
    },
};
auth.init();
