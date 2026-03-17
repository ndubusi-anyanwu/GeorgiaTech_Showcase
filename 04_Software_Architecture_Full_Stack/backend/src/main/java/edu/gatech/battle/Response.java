package edu.gatech.battle;

public class Response {
    private String Message;
    public String getMessage() {
        return Message;
    }

    private boolean isSuccess;
    public boolean getIsSuccess() {
        return isSuccess;
    }

    public Response(String message, boolean isSuccess){
        this.Message = message;
        this.isSuccess = isSuccess;
    }
}
