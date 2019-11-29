<template>
  <div class="login">
    <h1>로그인 페이지 입니다.</h1>
    <LoginForm/>
  </div>
  
</template>

<script>
// @ -> alias to src
import LoginForm from '@/components/LoginForm'

export default {
  name:'Login',
  components:{
    LoginForm,
  }
}
</script>

<style>

</style>