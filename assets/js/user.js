var user = {
    init: function () {
        var _this = this;

        $("#frm_regist").on("submit", _this.handleSubmit);
    },
    handleSubmit: function (e) {
        e.preventDefault();

        try {
            var $form = $(this);
            var email_regex = new RegExp("[a-z0-9]+@[a-z]+.[a-z]{2,3}");
            var data = {
                name: $('[name="name"]', $form).val().trim(),
                email: $('[name="email"]', $form).val().trim(),
                password: $('[name="password"]', $form).val().trim(),
                password_chk: $('[name="password_chk"]', $form).val().trim(),
            };

            if (data.email.length === 0) {
                alert("이메일을 입력해주세요!!");
            } else if (!email_regex.test(data.email)) {
                alert("올바른 이메일을 입력해주세요!!");
            } else if (data.name.length === 0) {
                alert("이름을 입력해주세요!!");
            } else if (data.password.length === 0) {
                alert("비밀번호를 입력해주세요!!");
            } else if (data.password.length === 0) {
                alert("비밀번호 확인을 입력해주세요!!");
            } else if (data.password !== data.password_chk) {
                alert("비밀번호와 비밀번호 확인이 맞지 않습니다!!");
            } else {
                $.ajax({
                    url: "/api/v1/user/",
                    type: "post",
                    dataType: "json",
                    contentType: "application/json",
                    data: JSON.stringify(data),
                    success: function (res) {
                        try {
                            if (res.success) {
                                alert("등록되었습니다!!");
                                location.href = "/";
                            } else {
                                throw new Error(res.message);
                            }
                        } catch (e) {
                            alert(e.message || "오류가 발생했습니다!!");
                        }
                    },
                    error: function (err) {
                        alert("오류가 발생했습니다!!");
                    },
                });
            }
        } catch (e) {
            alert("오류가 발생했습니다");
        }

        return false;
    },
};
user.init();
