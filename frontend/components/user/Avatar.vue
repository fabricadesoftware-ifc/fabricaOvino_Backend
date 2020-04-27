<template>
  <div class="tile is-parent">
    <div class="tile is-child is-3">
      <strong>Avatar público</strong>
      <p>
        Você pode enviar o seu avatar aqui ou alterá-lo em
        <strong>gravatar.com</strong>
      </p>
    </div>
    <div class="tile is-child is-8 user-avatar">
      <Gravatar :email="email" :size="200" alt="user" />
    </div>
  </div>
</template>

<script>
import Gravatar from 'vue-gravatar'
export default {
  components: { Gravatar },
  props: ['email']

}
</script>

<style>
.user-avatar img {
  border-radius: 100px;
  align-self: center;
}
</style>
