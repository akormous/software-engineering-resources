#ifndef GENERIC_DISPLAY_HPP
#define GENERIC_DISPLAY_HPP

#include "Display.hpp"
#include "Observer.hpp"
#include "Subject.hpp"
#include "WeatherStation.hpp"
/**
 * A generic display app that implements Display and Observer interface
*/
class GenericDisplay : public Observer, Display {
public:
    GenericDisplay();
    void update(Subject* weatherStation) override;
    void display() override;

private:
    Subject* subject;
    float temp;
    float humidity;
};

#endif // GENERIC_DISPLAY_HPP