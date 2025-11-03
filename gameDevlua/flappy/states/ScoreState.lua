--[[
    ScoreState Class
    Author: Colton Ogden
    cogden@cs50.harvard.edu

    A simple state used to display the player's score before they
    transition back into the play state. Transitioned to from the
    PlayState when they collide with a Pipe.
]]

ScoreState = Class{__includes = BaseState}

--[[
    When we enter the score state, we expect to receive the score
    from the play state so we know what to render to the State.
]]

-- Loads in images of diff medal variables 
local medals = {
    ['bronze'] = love.graphics.newImage('bronzeMedal.png'),
    ['silver'] = love.graphics.newImage('silverMedal.png'),
    ['gold'] = love.graphics.newImage('goldMedal.png')
}

medal = love.graphics.newImage('bird.png')

local medalName = "bronze"
local message = ""
local medalWidth = 0
local medalHeight = 0

function ScoreState:enter(params)
    self.score = params.score
end

function ScoreState:update(dt)
    -- initialises the message
    message = "Oof! You lost!"
    -- go back to play if enter is pressed
    if love.keyboard.wasPressed('enter') or love.keyboard.wasPressed('return') then
        gStateMachine:change('countdown')
    end
    
    -- changes name and message according to score
    if self.score >= 3 and self.score < 6 then
        medalName = "bronze"
        message = "Almost there!"
    elseif self.score >= 6 and self.score < 10 then
        medalName = "silver"
        message = "Keep it up!"
    elseif self.score >= 10 then
        medalName = "gold"
        message = "Amazing job!"
    end

    medalWidth = medals[medalName]:getWidth()

end

function ScoreState:render()
    -- simply render the score to the middle of the screen
    love.graphics.setFont(flappyFont)
    
    -- renders the message according to the score
    love.graphics.printf(message, 0, 64, VIRTUAL_WIDTH, 'center')
    
    love.graphics.setFont(mediumFont)
    love.graphics.printf('Score: ' .. tostring(self.score), 0, 100, VIRTUAL_WIDTH, 'center')

    -- renders the medal picture according to the score
    if self.score >= 3 then
        love.graphics.draw(medals[medalName], (VIRTUAL_WIDTH - medalWidth / 20) / 2, 120, 0, 0.05, 0.05)
    end

    love.graphics.printf('Press Enter to Play Again!', 0, 160, VIRTUAL_WIDTH, 'center')
end