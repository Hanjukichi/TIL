# Ⅰ. 시작하기

## 1. 프로젝트 시작
- java, android studio 등이 설치 및 세팅되어있어야함.  
- [참고 링크](https://velog.io/@thovy/React-Native-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-1)
```
npx react-native@latest init [프로젝트 이름]
```

## 2. 프로젝트 실행
```
npm start
```
```
r - reload the app
d - open developer menu
i - run on iOS
a - run on Android
```

<br>

# Ⅱ. Routing

## 1. 설치하기
```
npm install @react-navigation/native @react-navigation/stack
```
``` bash
npm install react-native-screens react-native-safe-area-context
```
``` java
// android/app/src/main/java/<your package name>/MainActivity.java 파일 수정
public class MainActivity extends ReactActivity {
  // 이 밑을 추가...
  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(null);
  }
  // ...
}
```

## 2. 기본 사용법
- `<NavigationContainer>` 컨테이너 안에 라우팅할 요소들 배치
- 스택형으로 배치할 거면 `createNativeStackNavigator()` 사용
  - 스택 : 라우팅 요소들을 종이 위에 종이를 올리 듯 겹쳐 올려서 표시
```javascript
// In App.js in a new project

import * as React from 'react';
import { View, Text } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { HomeScreen, DetailsScreen } from 'src/component'

const Stack = createNativeStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Details" component={DetailsScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
```

## 3. 라우터끼리의 이동
1. 우선 이동할 스크린들을 정의
```ts
// types.tsx
import type { NativeStackScreenProps } from '@react-navigation/native-stack';

type RootStackParamList = {
  Start: undefined,
  Login: undefined,
};

export type routeProps = NativeStackScreenProps<RootStackParamList>;
```
2. 정의된 타입을 기반으로 스크린간 이동 함수 정의
```ts
...
import { routeProps } from '../types/propsTypes';

const StartView = ({navigation}:routeProps):JSX.Element => {
  ...
  // 터치하면 화면 이동
  const routeLogin = () => {
    navigation.navigate("Login");
  };

  return (
    <TouchableOpacity  style={Startstyles.totalBox} onPress={routeLogin}>
    ...
    </TouchableOpacity>
  );
};

export default StartView;

```


## 4. safe area
- ios 노치를 위한 기능
```tsx
// 기본 요소 import
import { SafeAreaProvider } from 'react-native-safe-area-context';

const Stack = createNativeStackNavigator();

function App(): JSX.Element {
  return (
    <SafeAreaProvider>
      ...
    </SafeAreaProvider>
  );
}

export default App;
```

<br>

# Ⅲ. 기타 태그들

## TouchableOpacity 태그
- `onPress` 이벤트를 사용하기 위해서 사용해야하는 태그
```ts
// 태그 import
import { TouchableOpacity } from 'react-native';
```


## 애니메이션 태그
- `Animated`라는 객체를 사용
-  `useRef`로 `Value`를 하나 만들어야 함.
- `Animated` 뒤에 사용하고 싶은 리액트 네이티브 컴포넌트를 넣어줌

```tsx
// 태그 import
import { 
Animated  
} from 'react-native';

const StartView = () => {
  ...
  const animatedMargin = useRef(new Animated.Value(110)).current;
  useEffect(() => {
    Animated.timing(animatedMargin, {
      toValue: 0,
      // 애니메이션의 지속시간 (1초)
      duration: 1000, 
      useNativeDriver: false, 
    }).start();
  }, []);
  ...

  return (
    <View style={Startstyles.totalBox}>
      ...
      <Animated.View style={{ ...Startstyles.startImg, marginTop: animatedMargin.interpolate({
        inputRange: [0, 110], // input 범위 설정
        outputRange: ['0%', '110%'], // output 범위 설정
      }) }}>
        ...
      </Animated.View>
    </View>
  );
};

export default StartView;
```

