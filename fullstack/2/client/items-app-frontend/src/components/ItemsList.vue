<template>
  <div>
    <h2>THE LIST</h2>

    <div>Counter: {{ counter }}</div>

    <button @click="incrementBtnClicked">increment counter</button>
  </div>
</template>
<script>
export default {
  methods: {
    incrementBtnClicked() {
      this.$store.dispatch("incrementBtnClicked");
    },
  },
  computed: {
    counter() {
      return this.$store.state.count;
    },
  },
};
</script>
<style></style>
