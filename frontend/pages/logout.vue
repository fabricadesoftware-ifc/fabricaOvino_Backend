<template>
  <section></section>
</template>

<script>
export default {
  async created() {
    await this.$auth.logout()
  }
}
</script>
