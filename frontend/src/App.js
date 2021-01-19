import './App.css';
import { BrowserRouter as Router,
          Route } from 'react-router-dom';

import Navbar from '../src/components/navbar/Navbar';
import Wrapper from '../src/components/wrapper/Wrapper';
import HomeScreen from '../src/screens/HomeScreen/HomeScreen';
import BioScreen from '../src/screens/BioScreen/BioScreen';
import GalleryScreen from '../src/screens/GalleryScreen/GalleryScreen';
import ShowsScreen from '../src/screens/ShowsScreen/ShowsScreen';
import VideoScreen from '../src/screens/VideosScreen/VideosScreen';

export default function App(){
  return(
    <Router>
        <Navbar/>
        <Wrapper>
            <Route exact path="/" component={HomeScreen}/>
            <Route exact path="/bio" component={BioScreen}/>
            <Route exact path="/gallery" component={GalleryScreen}/>
            <Route exact path="/live" component={ShowsScreen}/>
            <Route exact path="/videos" component={VideoScreen}/>
        </Wrapper>
    </Router>
  )
}
