<template>
  <div class="tile is-parent">
    <div class="tile is-child is-3">
      <strong>Grupos</strong>
    </div>
    <div class="tile is-child is-9 groups">
      <div class="select-groups">
        <b-field>
          <b-select
            multiple
            size="10"
            native-size="10"
            v-model="selectGroupFrom"
          >
            <option
              v-for="group in groups_from"
              :key="group.id"
              :value="group.id"
              >{{ group.name }}</option
            >
          </b-select>
        </b-field>
        <b-button
          type="is-info"
          @click="selectAllGroups"
          icon-right="arrow-right-bold-outline"
          >Escolher todos</b-button
        >
      </div>
      <div class="select-buttons">
        <b-button
          type="is-info"
          @click="selectGroup"
          icon-right="arrow-right-bold-outline"
        ></b-button>
        <b-button
          type="is-info"
          @click="removeGroup"
          icon-right="arrow-left-bold-outline"
        ></b-button>
      </div>
      <div class="select-groups">
        <b-field>
          <b-select multiple native-size="10" v-model="selectGroupTo">
            <option
              v-for="group in choosed_groups"
              :key="group.id"
              :value="group.id"
              >{{ group.name }}</option
            >
          </b-select>
        </b-field>
        <b-button
          type="is-info"
          @click="removeAllGroups"
          icon-right="arrow-left-bold-outline"
          >Remover todos</b-button
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    choosedIds: Array,
    edit: {
      type: Boolean,
      default() {
        return false
      }
    }
  },
  data() {
    return {
      selectGroupFrom: [],
      selectGroupTo: [],
      groups: []
    }
  },
  async fetch() {
    this.groups = await this.$axios.$get('/api/v1/groups/')
  },
  computed: {
    groups_from() {
      let choosed = this.choosedIds

      var groups = this.groups.filter(function (group) {
        return choosed.includes(group.id) == false
      })
      return groups
    },
    choosed_groups() {
      let choosed = this.choosedIds
      var groups = this.groups.filter(function (group) {
        return choosed.includes(group.id)
      })
      return groups
    }
  },
  methods: {
    selectGroup() {
      this.choosedIds = [...this.choosedIds, ...this.selectGroupFrom]
      this.selectGroupFrom = []
      this.$emit('update-choosed', this.choosedIds)
    },
    selectAllGroups() {
      this.choosedIds = [
        ...this.choosedIds,
        ...this.groups_from.map(({ id }) => id)
      ]
      this.selectGroupFrom = []
      this.$emit('update-choosed', this.choosedIds)
    },
    removeGroup() {
      this.choosedIds = this.choosedIds.filter(
        id => !this.selectGroupTo.includes(id)
      )
      this.selectGroupTo = []
      this.$emit('update-choosed', this.choosedIds)
    },
    removeAllGroups() {
      this.choosedIds = []
      this.selectGroupTo = []
      this.$emit('update-choosed', this.choosedIds)
    }
  }
}
</script>

<style>
.groups {
  display: flex;
  height: 400px;
}
.select-groups {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 40%;
}

.select-buttons {
  display: flex;
  flex-direction: column;
  padding: 10px;
  margin-top: 100px;
}

.select-buttons button {
  margin-bottom: 10px;
}
</style>
