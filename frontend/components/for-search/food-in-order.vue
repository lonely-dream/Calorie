<template>
	<view v-if=weight class="FoodInOrder">
		<view class="FoodName">{{foodname}}</view>
		<view style="color:#FFFFFF;" class="Calories">{{calorie}}kcal</view>
		<button class="ButtonInOrder" @tap="MinusWeight">-</button>
		<view class="Weight">{{weight}}</view>
		<button class="ButtonInOrder" @tap="AddWeight">+</button>
	</view>
</template>

<script>
	export default {
		props: {
			foodname: {
				type: String,
				default: "None",
			},
			calorie: {
				type: Number, 
				default: 0,
			},
      weight: {
        type: Number,
        default: 0,
      }
		},
		data() {
			return {
			}
		},
		methods: {
			MinusWeight() {
				var ordered_food = uni.getStorageSync("meal-list");
				for(var i = 0; i < ordered_food.length; i++) {
				  var f = ordered_food[i];
				  if(f.name === this.foodname) {
				    //f.cal -= f.cal / f.sum * 50;
            if(f.sum > 0) {
              f.sum -= 1;
              uni.setStorageSync("meal-list", ordered_food);
              uni.$emit("refresh1");
              uni.$emit("refresh2");
            }
				    return;
				  }
				}
				uni.$emit("refresh");
			},
			AddWeight() {
        var ordered_food = uni.getStorageSync("meal-list");
        console.log("ordered_food:");
        console.log(ordered_food);
        for(var i = 0; i < ordered_food.length; i++) {
          var f = ordered_food[i];
          if(f.name === this.foodname) {
           // f.cal += f.cal / f.sum * 50;
            f.sum += 1;
            ordered_food[i] = f;
            console.log("ordered_food:");
            console.log(ordered_food);
            uni.setStorageSync("meal-list", ordered_food);
            uni.$emit("refresh1");
            uni.$emit("refresh2");
            return;
          }
        }
			}
		},
	}
</script>

<style>
	.FoodInOrder {
		position: relative;
		width: 100%;
		font-size: 30rpx;
	}
	.FoodName {
		text-align: left;
		width: 40%;
		display: inline-block;
	}
	.Calories {
		text-align: left;
		width: 20%;
		display: inline-block;
	}
	.ButtonInOrder {
	    font-size: 35rpx;
	    height: 45rpx;
	    width: 45rpx;
        border-radius: 50%;
	    display: inline-block;
        color: #fff;
        background-color: rgba(89, 69, 61, 1);
        line-height: 45rpx;
        padding: 0;
        margin:0 5rpx;
	}
	.Weight {
		text-align: center;
		width: 10%;
		display: inline-block;
    vertical-align:top;
	}
</style>
