weather_conditions=["sunny","rainy","cold"]
recommendations=["Wear a t-shirt and sunglasses","Don't forget your umbrella and a raincoat.","Make sure to wear a warm coat and a scarf","Sorry, I don't have recommendations for this weather."]
selected_weather = input("What's the weather like today? (sunny/rainy/cold): ")
if (selected_weather == weather_conditions[0]) : {
    print (recommendations[0])
}
elif selected_weather == weather_conditions[1] : {
    print (recommendations[1])
} 
elif selected_weather == weather_conditions[2] : {
    print (recommendations[2])
} 
else : {
    print (recommendations[3])
}

